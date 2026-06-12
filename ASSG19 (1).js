import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  StatusBar,
  SafeAreaView,
} from 'react-native';

export default function App() {
  // State 1: Counter value
  const [count, setCount] = useState(0);

  // State 2: Theme toggle
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Counter functions
  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleDecrement = () => {
    if (count > 0) {
      setCount(count - 1);
    }
    // If count is already 0, do nothing (no negative values)
  };

  const handleReset = () => {
    setCount(0);
  };

  // Theme toggle function
  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

  // Dynamic theme styles using ternary operators
  const themeStyles = {
    container: {
      backgroundColor: isDarkMode ? '#1a1a1a' : '#ffffff',
    },
    titleText: {
      color: isDarkMode ? '#ffffff' : '#1a1a1a',
    },
    counterText: {
      color: isDarkMode ? '#00e5ff' : '#1565c0',
    },
    labelText: {
      color: isDarkMode ? '#aaaaaa' : '#555555',
    },
    themeButton: {
      backgroundColor: isDarkMode ? '#f0f0f0' : '#1a1a1a',
    },
    themeButtonText: {
      color: isDarkMode ? '#1a1a1a' : '#ffffff',
    },
  };

  return (
    <SafeAreaView style={[styles.safeArea, themeStyles.container]}>
      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        backgroundColor={isDarkMode ? '#1a1a1a' : '#ffffff'}
      />

      <View style={[styles.container, themeStyles.container]}>

        {/* App Title */}
        <Text style={[styles.title, themeStyles.titleText]}>
          Digital Counter
        </Text>

        {/* Theme Toggle Button */}
        <TouchableOpacity
          style={[styles.themeButton, themeStyles.themeButton]}
          onPress={toggleTheme}
          activeOpacity={0.8}
        >
          <Text style={[styles.themeButtonText, themeStyles.themeButtonText]}>
            {isDarkMode ? '☀️  Light Mode' : '🌙  Dark Mode'}
          </Text>
        </TouchableOpacity>

        {/* Counter Display Card */}
        <View style={[
          styles.counterCard,
          { backgroundColor: isDarkMode ? '#2c2c2c' : '#f0f4ff' }
        ]}>
          <Text style={[styles.counterLabel, themeStyles.labelText]}>
            CURRENT COUNT
          </Text>
          <Text style={[styles.counterValue, themeStyles.counterText]}>
            {count}
          </Text>
        </View>

        {/* Increment & Decrement Buttons - Side by Side */}
        <View style={styles.rowButtons}>
          <TouchableOpacity
            style={[styles.button, styles.decrementButton,
              count === 0 && styles.disabledButton
            ]}
            onPress={handleDecrement}
            activeOpacity={count === 0 ? 1 : 0.8}
          >
            <Text style={styles.buttonText}>−</Text>
            <Text style={styles.buttonLabel}>Decrement</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.button, styles.incrementButton]}
            onPress={handleIncrement}
            activeOpacity={0.8}
          >
            <Text style={styles.buttonText}>+</Text>
            <Text style={styles.buttonLabel}>Increment</Text>
          </TouchableOpacity>
        </View>

        {/* Reset Button */}
        <TouchableOpacity
          style={[styles.button, styles.resetButton]}
          onPress={handleReset}
          activeOpacity={0.8}
        >
          <Text style={styles.buttonText}>↺</Text>
          <Text style={styles.buttonLabel}>Reset</Text>
        </TouchableOpacity>

        {/* Status message */}
        <Text style={[styles.statusText, themeStyles.labelText]}>
          {count === 0
            ? 'Counter is at zero'
            : count === 1
            ? '1 step counted!'
            : `${count} steps counted!`}
        </Text>

      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 24,
  },
  title: {
    fontSize: 32,
    fontWeight: '800',
    letterSpacing: 1,
    marginBottom: 20,
  },
  themeButton: {
    paddingVertical: 10,
    paddingHorizontal: 24,
    borderRadius: 25,
    marginBottom: 40,
  },
  themeButtonText: {
    fontSize: 15,
    fontWeight: '600',
  },
  counterCard: {
    width: '100%',
    borderRadius: 20,
    paddingVertical: 40,
    alignItems: 'center',
    marginBottom: 40,
    elevation: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.15,
    shadowRadius: 8,
  },
  counterLabel: {
    fontSize: 13,
    fontWeight: '600',
    letterSpacing: 2,
    marginBottom: 12,
  },
  counterValue: {
    fontSize: 80,
    fontWeight: '900',
    lineHeight: 90,
  },
  rowButtons: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    gap: 16,
    marginBottom: 16,
  },
  button: {
    flex: 1,
    borderRadius: 16,
    paddingVertical: 18,
    alignItems: 'center',
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
  incrementButton: {
    backgroundColor: '#1565c0',
  },
  decrementButton: {
    backgroundColor: '#c62828',
  },
  disabledButton: {
    backgroundColor: '#9e9e9e',
    elevation: 0,
  },
  resetButton: {
    width: '100%',
    backgroundColor: '#2e7d32',
    marginBottom: 24,
  },
  buttonText: {
    fontSize: 28,
    fontWeight: '800',
    color: '#ffffff',
    lineHeight: 32,
  },
  buttonLabel: {
    fontSize: 12,
    fontWeight: '600',
    color: '#ffffff',
    marginTop: 4,
    letterSpacing: 0.5,
  },
  statusText: {
    fontSize: 14,
    fontStyle: 'italic',
  },
});
