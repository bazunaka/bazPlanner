using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using static bazPlannerWPF.sqlite_connect;
using static bazPlannerWPF.auth;
using System.IO;

namespace bazPlannerWPF
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            DateTime now = DateTime.Now;
            Now_time.Content = now.ToString("D");
            
            if(sqlite_connect.Connect("test.db"))
            {
                Console.WriteLine("Connected!");
            }

            //File.AppendAllText("log.txt", Environment.NewLine); логирование потом!
        }

        private void Connect_to_DB(object sender, RoutedEventArgs e)
        {
            if(CheckAuth() == 0)
            {
                auth f = new auth(); //переименовать
                f.Show();
            }
            
        }

        private void Create_project(object sender, RoutedEventArgs e)
        {
            Console.WriteLine("Created!");
        }
    }
}
