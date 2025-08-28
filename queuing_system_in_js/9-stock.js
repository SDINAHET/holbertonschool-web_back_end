import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// ====================
// Data
// ====================
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Utility: get item by ID
function getItemById(id) {
  return listProducts.find((item) => item.itemId === id);
}

// ====================
// Redis client
// ====================
const client = redis.createClient();

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

// Reserve stock in Redis
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

// Get current reserved stock
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : null;
}

// ====================
// Express server
// ====================
const app = express();
const PORT = 1245;

// Route: list all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route: get details of one product
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    reservedStock !== null ? reservedStock : item.initialAvailableQuantity;

  res.json({ ...item, currentQuantity });
});

// Route: reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    reservedStock !== null ? reservedStock : item.initialAvailableQuantity;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: item.itemId });
  }

  await reserveStockById(itemId, currentQuantity - 1);
  return res.json({ status: 'Reservation confirmed', itemId: item.itemId });
});

// Start server
app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});
