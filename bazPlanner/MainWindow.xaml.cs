using System;
using System.Windows;
using bazPlanner.Models;

namespace bazPlanner
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            //Connect to database.
            Database.Connect();
            //Now time.
            DateTime now = DateTime.Now;
            labelTime.Content = now.ToString("D");
        }
    }
}
