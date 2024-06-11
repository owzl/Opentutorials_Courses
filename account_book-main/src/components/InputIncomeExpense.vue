<template>
  <div>
    <form @submit.prevent="handleAddAccount">
      <div>
        <label for="date">Date:</label>
        <input type="date" v-model="form.date" required />
      </div>
      <div>
        <label for="type">Type:</label>
        <select v-model="form.type" @change="updateCategories">
          <option value="income">Income</option>
          <option value="expense">Expense</option>
        </select>
      </div>
      <div>
        <label for="category">Category:</label>
        <select v-model="form.category">
          <option
            v-for="category in categories"
            :key="category"
            :value="category"
          >
            {{ category }}
          </option>
        </select>
      </div>
      <div>
        <label for="title">Title:</label>
        <input type="text" v-model="form.title" required />
      </div>
      <div>
        <label for="amount">Amount:</label>
        <input type="text" v-model="form.amount" required />
      </div>
      <button type="submit">Add</button>
    </form>
    <ul>
      <li v-for="account in accountList" :key="account.id">
        {{ account.date }} - {{ account.type }} - {{ account.category }} -
        {{ account.title }} - {{ account.amount }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue';
import { useAccountListStore } from '../stores/account';

const form = reactive({
  date: '',
  type: 'income',
  category: '',
  title: '',
  amount: '',
});

const categories = ref([]);

const accountStore = useAccountListStore();
const { accountList, fetchAccountList, addAccount } = accountStore;

const successCallback = () => {
  alert('Account successfully added!');
};

const handleAddAccount = async () => {
  const payload = { ...form, id: Date.now() };
  await addAccount(payload, successCallback);
};

const updateCategories = () => {
  if (form.type === 'income') {
    categories.value = ['salary', 'pin', 'etc'];
  } else {
    categories.value = ['fixed expenditure', 'culture', 'life', 'etc'];
  }
  form.category = categories.value[0];
};

onMounted(() => {
  updateCategories();
  fetchAccountList();
});
</script>

<style>
#input_wrap {
  display: flex;
  flex-direction: row;
  background-color: white;
  border-radius: 10px;
  margin-top: 20px;
  justify-content: space-between;
}
#date {
  width: 180px;
}
#type {
  width: 170px;
}
#category {
  width: 180px;
}
#title {
  width: 400px;
}
</style>
