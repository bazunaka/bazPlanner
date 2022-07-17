using System;
using System.Windows;
using bazPlanner.Models;
using bazPlanner.Forms;

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

        //Show form fot auth.
        private void FormAuth(object sender, RoutedEventArgs e)
        {
            Auth authWindow = new()
            {
                Owner = this
            };
            authWindow.Show();
        }

        private void AddProject(object sender, RoutedEventArgs e)
        {
            Database.InsertProject();
        }
    }
}
